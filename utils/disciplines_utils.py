import json

from pydantic.json import pydantic_encoder

from model.pydantic.discipline_works import DisciplinesConfig, DisciplineWorksConfig


def load_disciplines_config(file_path: str) -> DisciplinesConfig:
    with open(file_path, encoding="utf-8") as json_file:
        disciplines_config = json.load(json_file)
    return DisciplinesConfig(**disciplines_config)


def disciplines_config_to_json(data: DisciplinesConfig) -> str:
    return json.dumps(
        data,
        sort_keys=False,
        indent=4,
        ensure_ascii=False,
        separators=(",", ": "),
        default=pydantic_encoder,
    )


def disciplines_config_from_json(json_data: str) -> DisciplinesConfig:
    disciplines_config = json.loads(json_data)
    return DisciplinesConfig(**disciplines_config)


def disciplines_works_to_json(data: DisciplineWorksConfig) -> str:
    return json.dumps(
        data,
        sort_keys=False,
        indent=4,
        ensure_ascii=False,
        separators=(",", ": "),
        default=pydantic_encoder,
    )


def load_discipline(downloaded_data: bytes) -> DisciplineWorksConfig:
    disciplines_config = json.loads(downloaded_data)
    return DisciplineWorksConfig(**disciplines_config)


def disciplines_works_from_json(json_data: bytes) -> DisciplineWorksConfig:
    disciplines_config = json.loads(json_data)
    return DisciplineWorksConfig(**disciplines_config)


def counting_tasks(discipline: DisciplineWorksConfig) -> int:
    return sum([it.amount_tasks for it in discipline.works])
