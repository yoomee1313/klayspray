#!/usr/bin/env python3
import subprocess
import argparse
from typing import Optional

class GCPCredentials:
    """
    GCP Credentials Login and Management
    """
    
    @staticmethod
    def login(project_id: Optional[str] = None) -> bool:
        """
        Login to GCP using gcloud
        
        :param project_id: Optional GCP project ID to set after login
        :return: Login status
        """
        try:
            # Trigger interactive login
            subprocess.run(["gcloud", "auth", "login"], check=True)
            
            if project_id:
                subprocess.run(["gcloud", "config", "set", "project", project_id], check=True)
            
            return True
        except subprocess.CalledProcessError:
            return False

def main():
    """
    Command-line interface for GCP login
    """
    parser = argparse.ArgumentParser(description='GCP Login Utility')
    parser.add_argument('-p', '--project', 
                        help='GCP Project ID to set after login', 
                        required=False)
    
    args = parser.parse_args()
    
    # Perform login
    success = GCPCredentials.login(project_id=args.project)
    
    # Exit with appropriate status code
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
