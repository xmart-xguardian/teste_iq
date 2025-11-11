# Git Checkout Procedure

```
1. git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/siq

2. Configurar o server Jboss AS 5.1
	Adicionar o server Jboss Community > Jboss AS 5.1
	
	Diretório do server: C:\Java\SIQ\server\jboss-as-5.2
	
	Alterar o TimeOut para 9999
	
	Alterar a memória conforme disponível no equipamento (recomendado minimo de 2048)
	
		VM arguments 
			-Xms2048m 
			-Xmx2048m

3. Enconding Eclipse

 Vá em: Window > Preferences

 Navegue até: General > Workspace

 Em Text file encoding, selecione: Other: e escolha Default (Windows-1252)

 Clique em Apply and Close

4. Para Build Maven 

 Goals: clean install
 Profiles: jboss siq
 
 JRE - VM Arguments
 
  -DjbossDeployPath=C:/Java/SIQ/server/jboss-as-5.2/server/default/deploy/siq_app.sar.last
  -DcompileJavaVersion=1.8
  -DaspectjrtVersion=1.8.13
  -Xms2048m

 Enviroments Variable
 
  VAULT_ADDRESS = https://vault.siq.com.br
  VAULT_TOKEN = <TOKEN> 
  
```

# Git Workflow and Commit Standards

## Git Workflow

This team follows a simplified Git Flow based on two primary branches: `main` and `develop`.

### Main Branches

```
Branch     | Purpose
---------- | ---------------------------------------------
main       | Production-ready code. Always stable.
develop    | Integration branch for features and fixes.
```

---

## Supporting Branches

```
Type          | Prefix            | Description
------------- | ----------------- | ---------------------------------------------
Feature       | feature/          | New features
Bugfix        | bugfix/           | Non-critical bug fixes
Hotfix        | hotfix/           | Critical production fixes
Improvement   | improvement/      | Refactors or performance improvements
```

---

## Commit Message Guidelines

Commit messages should follow the format:

```
<type>: <brief description> (#task_id)
```

### Allowed Commit Types

```
Type      | Description
--------- | -----------------------------------------------------------
feat      | A new feature
fix       | A bug fix
refactor  | Code changes that neither fix a bug nor add a feature
perf      | Performance improvements
style     | Code formatting, no logic changes
test      | Adding or modifying tests
docs      | Documentation changes
chore     | Maintenance tasks (e.g., dependencies, config updates)
```

### Examples

```bash
feat: add logout functionality (#123)
fix: resolve discount calculation issue (#117)
refactor: extract authentication logic to service layer (#134)
```

---

## Typical Development Flow

```bash
# 1. Switch to the development branch
git checkout develop
git pull origin develop

# 2. Create a new feature branch
git checkout -b feature/user-registration

# 3. After making changes, stage and commit
git add .
git commit -m "feat: implement user registration flow (#56)"

# 4. Push the feature branch to the remote repository
git push origin feature/user-registration

# 5. After review and merge
git checkout develop
git pull origin develop
git merge feature/user-registration # Merge the feature into develop
git push origin develop # Push the updated develop branch to the remote repository

# 6. Delete local and remote branches
git branch -d feature/user-registration
git push origin --delete feature/user-registration


```

---

## Release Flow

# 1. Merge develop into master
git checkout master
git pull origin master # Make sure master is up to date
git merge develop # Merge develop into master
git push origin master # Push the updated master branch to the remote repository, put the client name on push message

# 2. Build Release
Access the AWS console
Access the codeBuild menu
Click on the siq-app-platform project
Click on Edit
In the Environment section, at the end of it, click on additional configuration and scroll down to the Environment variables section
Generate a token or copy an existing one from the Vault and place it in the VAULT_TOKEN variable
In the MAVEN_PROFILES variable, place the profiles according to the desired build
Scroll down to the end of the screen and click on Update Project
When you return to the project screen, click on START BUILD. The build screen will open, where you can monitor the execution using the tail logs button
When finished, the war will be generated in the siqsystemsbuild bucket inside the build folder. It contains the version.properties that are inside the war, to check the version and compiled client
Now download and continue with the update

# 2. Build Fixes
Access the AWS console
Access the codeBuild menu
Click on the project siq-app-platform-fixes
click on Edit
In the Source section, in the Branch field, select the fixes Branch
In the Environment section, at the end of it, click on additional configuration and scroll down to the Environment variables section
Generate a token or copy an existing one in the Vault and place it in the VAULT_TOKEN variable
In the MAVEN_PROFILES variable, place the profiles according to the desired build
Scroll down to the end of the screen and click on Update Project
When you return to the project screen, click on START BUILD, the build screen will open, where you can follow the execution using the tail logs button
When finished, the war will be generated in the siqsystemsbuild bucket inside the build-fixes folder, which contains the version.properties that is inside the war, to check the version and compiled client
Now download and continue with the update

Note: Both the version in the pom, as well as the generation of the tag, will be done automatically by the build

If need to delete a remote tag
git push origin :refs/tags/v8.1.5.0.20250514.16


---

## Additional Notes

- Avoid vague commit messages like `fixes`, `updates`, or `changes`.
- Never merge directly into `master`; 

## SIQ

**Version Information**

As per the resolution, for security reasons the versions of some libs are omitted, so in this document we must always keep the versions updated for future changes and maintenance.

**JQuery**
Richfaces= 2.2.4
Vendor= 3.7.1