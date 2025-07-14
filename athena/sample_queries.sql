SELECT
  json_extract_scalar(message, '$.developer') AS developer,
  json_extract_scalar(message, '$.service') AS service,
  json_extract_scalar(message, '$.event_type') AS event_type,
  json_extract_scalar(message, '$.outcome') AS outcome,
  json_extract_scalar(message, '$.duration_sec') AS duration
FROM dora_logs
WHERE dt = '2025-07-14';
