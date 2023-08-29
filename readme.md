## Create an API User in FortiCloud

For the procedure to configure a connector, follow the steps below. 

1. Login to https://support.fortinet.com.
2. Click **Services**, then under "Assets & Accounts" click **IAM**.
![IAM Option](/docs/images/iam.png)

3. On the left pane, click **Permission Profiles**

    ![Permission Profiles](/docs/images/permission_profiles.png)

5. Click **Add New**

    ![Add New Button](/docs/images/add_new.png)

7. Click **Add Portal**

    ![Add Portal Button](/docs/images/add_portal.png)

8. Check the box to the left of **Asset Management** and click **Add**
![Add Asset management permission](/docs/images/check_asset_management.png)

9. Provide a **Permission Profile Name**. This example will use `FortiSOAR Asset Management`
10. Toggle the **Access** slider to enable the portal, then click **Read/Write** option, then click the **Submit** button to save
![Add Asset management permission](/docs/images/enable_portal.png)

11. Navigate to the Users Section as seen from the image on step 3
12. Click **Add New > API User** 

    ![Add API User](/docs/images/add_api_user.png)
14. Select the **Permission Profile** `FortiSOAR Asset Management` , then click Next
![Assign Profile](/docs/images/assign_profile.png)
15. Click Confirm 
16. Download the credentials for the api user. These are required to configure the connector

    ![img.png](/docs/images/download_creds.png)
17. Provide a password to encrypt the file, then click **Proceed**
![img](/docs/images/protect_credentials.png)

## Configure the Connector
1. Locate the downloaded credentials for the API User
2. Open the file with the password used to encrypt the file.
3. Open the **FortiCloud Asset Management** connector from the content Hub
4. Fill in the required fields for the connector
