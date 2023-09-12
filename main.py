import boto3

def get_asg_suspended_processes(access_key, secret_key, security_token, region):
    try:
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=security_token,
            region_name=region
        )
        
        client = session.client('autoscaling')
        response = client.describe_auto_scaling_groups()

        for asg in response['AutoScalingGroups']:
            asg_name = asg["AutoScalingGroupName"]
            suspended_processes = asg.get("SuspendedProcesses", [])
            
            if suspended_processes:
                print("Name of Auto Scaling Group:", asg_name)
                
                for process in suspended_processes:
                    sus_Process = process["ProcessName"]
                    sus_time = process.get("SuspensionReason", "N/A")
                    print("Suspended Process:", sus_Process)
                    print("Suspended time:", sus_time)
                print()
            else:
                print("No suspended processes in Auto Scaling Group:", asg_name)
                
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    access_key = input("Please enter the Access key: ")
    secret_key = input("Please enter the Secret key: ")
    security_token = input("Please enter the Security token: ")
    region = input("Please enter the Region name: ")

    print()
    get_asg_suspended_processes(access_key, secret_key, security_token, region)
