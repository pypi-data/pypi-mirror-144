from enum import Enum
from typing import List, Optional

import pandas as pd
from pydantic import BaseModel
from pydantic.class_validators import validator
from pydantic.fields import Field

from exodusutils import internal
from exodusutils.schemas import Column


class TrainReqBody(BaseModel):
    """
    The base schema for training requests.
    """

    training_data: bytes = Field(description="The training data as a sequence of bytes")
    feature_types: List[Column] = Field(
        default=[], description="The features present in training data"
    )
    target: Column = Field(
        description="The target column. Must be present in feature_types"
    )
    folds: int = Field(
        default=5, ge=2, le=10, description="Number of folds for this experiment"
    )
    validation_percentage: float = Field(
        default=0.0, ge=0.0, lt=1.0, description="The validation percentage"
    )
    holdout_data: Optional[bytes] = Field(
        default=None, description="The holdout data as a sequence of bytes. Optional"
    )

    class Config:
        schema_extra = {
            "examples": [
                {
                    "training_data": "foo,bar\n0,abc\n1,def\n2,ghi\n3,jkl\n4,mnop\n5,qrs\n",
                    "feature_types": [
                        {"name": "foo", "data_type": "double"},
                        {"name": "bar", "data_type": "string"},
                    ],
                    "target": [{"name": "bar", "data_type": "string"}],
                    "folds": 3,
                    "validation_percentage": 0.2,
                    "holdout_data": "foo,bar\n99,zzz\n",
                }
            ]
        }

    @validator("target")
    def check_column(cls, v, values):
        if v not in values.get("feature_types", []):
            raise ValueError(
                f"target {v} not found in feature_types {values.get('feature_types', [])}"
            )
        return v

    @validator("feature_types")
    def validate_header(cls, v, values):
        data = values["training_data"]
        header = data.decode("utf-8").split("\n")[0].split(",")
        internal.validate_columns(header, v)
        return v

    def get_feature_names(self) -> List[str]:
        """
        Returns the names of the features.
        """
        return [f.name for f in self.feature_types]

    def get_training_df(self) -> pd.DataFrame:
        """
        Returns the Pandas DataFrame from the bytes in training_data field.
        """
        return internal.get_df(self.training_data, self.feature_types)

    def get_holdout_data(self) -> Optional[pd.DataFrame]:
        """
        Returns the Pandas DataFrame from the bytes in holdout_data field, or `None` if none specified.
        """
        if not self.holdout_data:
            return None
        else:
            return internal.get_df(self.holdout_data, self.feature_types)


class PredictReqBody(BaseModel):
    """
    The schema for prediction request body.
    """

    model_id: str = Field(description="The specified model id")
    data: str = Field(description="The prediction data as JSON")
    threshold: Optional[float] = Field(
        default=None, description="The threshold for classification predictions"
    )
    keep_columns: List[str] = Field(
        default=[], description="The columns to keep in the prediction response"
    )

    def get_prediction_df(self, feature_types: List[Column]) -> pd.DataFrame:
        """
        Returns the Pandas DataFrame from the bytes in data field.

        If the input data contains any column that is not in `feature_types`, that column will be
        dropped from the resulting dataframe.
        """
        valid_columns = [f.name for f in feature_types]
        df = pd.DataFrame(pd.read_json(self.data, orient="records"))
        valid_features = [f for f in feature_types if f.name in df.columns.tolist()]

        # We only want to keep the columns that are specified in `feature_types`
        return df.drop([c for c in df.columns.tolist() if c not in valid_columns], axis=1).pipe(
            internal.cast_df_types, valid_features
        )

class MigrateAction(str, Enum):
    """
    Defines the migration action. Could only be either one of `up` and `down`.
    """
    up = "up"
    down = "down"


class MigrateReqBody(BaseModel):
    """
    The schema for migrate request body.
    """

    action: MigrateAction = Field(description="The migration action")

    class Config:
        use_enum_values = True
