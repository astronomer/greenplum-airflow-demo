SELECT {{ params.state }}
FROM covid_state_data
WHERE date = {{ yesterday_ds_nodash}}