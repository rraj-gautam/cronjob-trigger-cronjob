# cronjob-trigger-cronjob
Cronjobs to trigger another cronjobs

1. A Flask Application that exposes the api or endpoints with response of timestamp
2. A 1st cronjob to call the api, get the timestamp and store it in mongodb
3. A 2nd cronjob to get the timestamp from mongodb and print in the log.

Note: 2nd Cronjob get triggered only after the 1st cronjob completes successfully.

# Implemnetaion Idea
- Use of SideCar/InitContainers. <br>
- Disable the 2nd cronjob to stop scheduling on any time. <br>
- Use `kubectl create job --from=cronjob/<cronjob_name>` to trigger the 2nd cronjob. But before triggering the 2nd cronjob, patch `suspend: false` inorder to make it runnable. <br>
- After triggering the 2nd cronjob, again patch it to `suspend: true`.
