from pydantic import BaseModel, ConfigDict, Field


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания для определенного курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление данных задания определенного курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = None
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None = Field(default=None, alias="minScore")
    order_index: int | None = Field(default=None, alias="orderIndex")
    description: str | None = None
    estimated_time: str | None = Field(default=None, alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения заданий определенного курса.
    """
    exercises: list[ExerciseSchema]


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания упражнения курса.
    """
    exercise: ExerciseSchema


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления упражнения курса.
    """
    exercise: ExerciseSchema

