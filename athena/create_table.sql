CREATE EXTERNAL TABLE IF NOT EXISTS dora_logs (
  message string
)
PARTITIONED BY (`dt` string)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://dora-metrics-logs/cloudwatch/'
TBLPROPERTIES ("classification"="json");
