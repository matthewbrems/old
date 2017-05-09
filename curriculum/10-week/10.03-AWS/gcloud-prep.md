## ![logo](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) GCloud Prep...

### Install Google Cloud DSK

We'll follow this step-by-step guide together:
https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version

You **do** want to do this!


```bash
gcloud config set disable_usage_reporting true
```

This is also a yes:

```bash
Modify profile to update your $PATH and enable shell command 
completion? (Y/n)? Y
```

You will also need to create some sample project/use the one Google Cloud suggests for you.

Check out our installation, and prve we need a GPU increase:

```bash
gcloud beta compute regions describe us-east1
```

### View Projects

Visit:

https://console.cloud.google.com/compute/quotas 

Once on your specific project, you need to request an increase in your limits.

### All set for the future.