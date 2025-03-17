# AzDo-fabric-cicd-sample to operationalize fabric-cicd to work with Microsoft Fabric and YAML Pipelines in Azure DevOps

Contains three different YAML files which can be used operationalize [fabric-cicd](https://github.com/microsoft/fabric-cicd) to work with Microsoft Fabric and YAML Pipelines in Azure DevOps. Based on a blog post I published that shows how to operationalize fabric-cicd to work with Microsoft Fabric and YAML Pipelines.

This repository caters for the three below scenarios.

1. [fabric-cicd-demo-variables.yml](/AzureDevOpstemplates/fabric-cicd-demo-variables.yml) - Pipeline that is fully orchestrated Azure Pipeline variables. For scenarios where all the values are constant.
2. [fabric-cicd-demo-wsparameters.yml](/AzureDevOpstemplates/fabric-cicd-demo-wsparameters.yml) - Pipeline that contains parameters that affect workspace values. Including workspace ID and items to deploy.
3. [fabric-cicd-demo-gblparameters.yml](/AzureDevOpstemplates/fabric-cicd-demo-gblparameters.yml) - Pipeline that contains global parameters. Suited for Option four in the recommended CI/CD options article by Microsoft.

You can find all the YAML files in the [AzureDevOpstemplate subfolder](/AzureDevOpstemplates). All of files contain details about what variables and/or prarameters are required for each one.

One quick way to get started is to [import the repository into Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/git/import-git-repository?view=azure-devops&WT.mc_id=DP-MVP-5004032%3Fview%3Dazure-devops). From there, [create a pipeline from an existing YAML file](https://xeladu.medium.com/how-to-create-a-pipeline-from-an-existing-yaml-file-in-azure-devops-4c41e74fde2b).

All of the samples of Fabric items provided in the worskpace folder are from the [original fabric-cicd repository](https://github.com/microsoft/fabric-cicd). However, I do recommend testing with your own items stored in a repository that is the backend for a workspace configured with Microsoft Fabric Git integration.

In addition, you can sutomize the ["parameter.yml" file](/workspace/parameter.yml) to suit your requirements.

This repository is provided "as is" based on the [MIT license](https://opensource.org/licenses/MIT). Basically, I am not responsible for your use of it.
