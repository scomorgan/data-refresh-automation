# Data Refresh Automation

This repository contains scripts and workflows for automating data refresh processes in Databricks. Below are the instructions on how to navigate the Databricks menus and use the features effectively.

## Table of Contents
- [Getting Started](#getting-started)
- [Navigating the Databricks Workspace](#navigating-the-databricks-workspace)
  - [Home](#home)
  - [Workspace](#workspace)
  - [Repos](#repos)
  - [Data](#data)
  - [Clusters](#clusters)
  - [Jobs](#jobs)
  - [SQL](#sql)
  - [Settings](#settings)
- [Running the Data Refresh Workflow](#running-the-data-refresh-workflow)

## Getting Started
To get started with Databricks, you need to have an account and access to a Databricks workspace. If you don't have an account, please contact your administrator.

## Navigating the Databricks Workspace

### Home
The Home menu is your personal space in Databricks. Here you can:
- Access your recent notebooks and jobs.
- View your personal files and folders.
- Manage your user settings.

### Workspace
The Workspace menu is where you can organize and access all your notebooks, libraries, and other files. It is structured in a hierarchical manner:
- **Users**: Contains personal folders for each user.
- **Shared**: Contains shared folders and notebooks accessible by multiple users.
- **Repos**: Contains version-controlled repositories linked to GitHub or other version control systems.

### Repos
The Repos menu allows you to manage your version-controlled repositories. You can:
- Clone repositories from GitHub.
- Commit and push changes.
- Manage branches and pull requests.

### Data
The Data menu is where you can manage your data sources. You can:
- Browse and explore datasets.
- Create and manage tables.
- Import data from various sources like S3, Azure Blob Storage, and more.

### Clusters
The Clusters menu is where you can create and manage clusters. Clusters are the computational resources used to run your notebooks and jobs. You can:
- Create new clusters.
- Start, stop, and restart clusters.
- Configure cluster settings and permissions.

### Jobs
The Jobs menu allows you to create and manage scheduled jobs. Jobs can be used to automate the execution of notebooks and workflows. You can:
- Create new jobs.
- Schedule jobs to run at specific times.
- Monitor job runs and view logs.

### SQL
The SQL menu is where you can create and manage SQL queries and dashboards. You can:
- Write and execute SQL queries.
- Create visualizations and dashboards.
- Manage SQL endpoints and permissions.

### Settings
The Settings menu allows you to configure various aspects of your Databricks workspace. You can:
- Manage user and group permissions.
- Configure workspace settings.
- Access audit logs and usage reports.

## Running the Data Refresh Workflow
To run the data refresh workflow, follow these steps:
1. **Open the Notebook**: Navigate to the `Data_Refresh_Workflow` notebook in the Workspace menu.
2. **Attach to a Cluster**: Ensure the notebook is attached to a running cluster.
3. **Run All Cells**: Click `Run All` to execute all cells in the notebook.
4. **Schedule the Job**: Go to the Jobs menu, create a new job, and schedule it to run the `Data_Refresh_Workflow` notebook at your desired frequency.

For more detailed instructions, refer to the individual sections above.

## Contributing
If you would like to contribute to this repository, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
