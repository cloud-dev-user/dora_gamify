aws logs create-export-task \
  --log-group-name "/dora/metrics" \
  --from <START_EPOCH> \
  --to <END_EPOCH> \
  --destination "dora-metrics-logs" \
  --destination-prefix "cloudwatch/"
