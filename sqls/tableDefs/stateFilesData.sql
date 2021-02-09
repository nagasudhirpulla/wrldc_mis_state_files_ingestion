CREATE TABLE "MIS_WAREHOUSE"."STATE_FILES_DATA" (
    "ID" NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY,
    "TIME_STAMP" DATE NOT NULL ENABLE,
    "ENTITY_TAG" VARCHAR2(100 BYTE) NOT NULL ENABLE,
    "METRIC_NAME" VARCHAR2(100 BYTE) NOT NULL ENABLE,
    "DATA_VALUE" NUMBER(*, 0),
    UNIQUE ("ENTITY_TAG", "METRIC_NAME", "TIME_STAMP")
)