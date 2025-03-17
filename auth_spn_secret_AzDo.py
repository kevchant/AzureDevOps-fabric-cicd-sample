# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
Example of authenticating with SPN + Secret
Can be expanded to retrieve values from Key Vault or other sources
"""
# Kevin Chant has extended this!!!
# START-EXAMPLE
# import from fabric_cicd and azure.identity to pass-through service principal
# from azure.identity import DefaultAzureCredential
from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items
import argparse
# import os


parser = argparse.ArgumentParser(description='Process some variables.')
parser.add_argument('--WorkspaceId', type=str)
parser.add_argument('--Environment', type=str)
parser.add_argument('--RepositoryDirectory', type=str)
parser.add_argument('--ItemsInScope', type=str)
args = parser.parse_args()

# Convert item_type_in_scope into a list
allitems = args.ItemsInScope
item_type_in_scope=allitems.split(",")
print(item_type_in_scope)


# Authenticate with DefaultAzureCredential authenticated by PowerShell
# credential = DefaultAzureCredential()

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id= args.WorkspaceId,
    environment=args.Environment,
    repository_directory=args.RepositoryDirectory,
    item_type_in_scope=item_type_in_scope,    
)

# # # Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)

# # # Unpublish all items defined in item_type_in_scope not found in repository
unpublish_all_orphan_items(target_workspace)
