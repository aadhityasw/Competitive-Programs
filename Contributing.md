**Coming Soon**
# Contributing

Before we get started with the technical details, Thank You for taking time to visit here. Whether you are willing to contribute to this repository, or are here to get the setup running on your local machine, this is the right place for that. So lets get started :)


## Setting up the Repository

Our first task would be to get the code in this repository onto your computer in order for you to start working easily. In order to simplify this process and to make it generic, I have used a few tools to keep this process the same for all, but there might be some errors or warnings in the process, so be ready to google them.

In case you do not have an Github account, go ahead and create one at [github.com](https://github.com). With this done head back to [this repository](https://github.com/aadhityasw/Competitive-Programs). If you are new to github, take some time to explore the options and the concepts related to git, version control, etc.

In order for you to modify the code from this repository and make your own changes, we would essentially `fork` my version of the repository into one which resides in your account, and you can make your changes there. Once you have made your changes and wish to observe those changes in this main repository, you would raise a `pull request`, but more on this later.


### Forking the Repository

1. Head over to the root repository, available [here](https://github.com/aadhityasw/Competitive-Programs).
2. Make sure, you are signed in into your account. Now click on the `Fork` option available there, and choose your account if served with a list of all organizations you are a part of.
3. Now you will be able to notice that the repository in fromt of you, would have `<YOUR_USER_NAME>/Competitive-Programs`. This is your forked version of the repository, and you can make any changes here without affecting the main repository.


### Installing Applications

1. Install [Github Desktop]() in your computer which would also install git along with it. Github Desktop provides an user-friendly interface to enable you to perform git commands without a command line interface.
2. It is to be noted that the Github Desktop Application is not available for linux. So in case you are using a linux machine, install the git command line tools from your terminal, and use git from your terminal. You would also have to authenticate into your account if you are using the CLI tool, and also link your username and email address so that the contributions you make from this system is reflected back in your account.
3. I would also suggest the use of [vs-code]() code editor for managing the codebase. I would prefer this because it has extensions which support docker and because I have created a vs-code development container for easier use.
4. In order for you to use the docker container, you would also have to install Docker on your computer. This can be done by installing the [Docker Desktop]() application.
5. Again if you are using an linux environment, this application would not be available, and so install docker command line tool, for using docker from your terminal.
6. Now in order to utilize the docker components installed, you would have to install a few extensions of vs-code, so open vs-code and head over to the `extensions` section from the left vertical bar. Now search and install the following extensions :
    * `Docker` from Microsoft
    * `Remote - Containers` from Microsoft


### Cloning your fork

With the required tools and applications installed, its time to get the codebase up and running.

You have now forked to make your own version of the repository, now you would just have to `clone` your forked version onto your computer to start working. Head back over to your forked version of your repository in your desktop, and follow the steps :

1. Click on the `Code` button from your forked version of the repository and click on `Open with Github Desktop` option if you have installed Github Desktop.
2. In case you want to use the CLI tools, then copy the URL shown there to set the repository up using HTTPS web URL. Then head over to your terminal and navigate to a location in your system where you want the codebase to be located, and then use the following command to clone the repository.
```bash
git clone https://github.com/<YOUR_USER_NAME>/Competitive-Programs.git
```
where `<YOUR_USER_NAME>` would be your github user account onto which you created your forked version.
3. Now you will be able to view the repository files on your computer.


### Running the Docker based Remote Container

With the codebase in your computer, the only step left is to run it. So follow the steps below to start coding.

1. Start the docker by either starting the docker desktop application or by using your teminal, and ensure that the server is up and running.
2. Open Vs-Code editor and then use the `Open Folder` option there to navigate to and choose the repository from your local computer, and open it.
3. Once the folder is open in vs-code, and if you have the previously mentioned extensions installed, you will get a prompt saying that this repository has a development container, and click to open the folder inside the container.
4. In case you do not get such a prompt, make sure that you have installed the mentioned extensions, and are visible in the left vertical bar. In this case click on the `Remote Containers` extension from the left bar, and you will find the option of `Open the current folder inside the development container`. Use this option to open your folder inside the container.
5. Once this is done, you will notice that the vs-code will fetch the docker image from my github continer registry, create a new volume and a container to run the codebase. If everything runs successfully, you will notice the bottom left of the vs-code to mention that you have opened the folder inside a docker container.
6. If you want to close this, click on that bottom left button or the `file` menu, and click on `close remote connection`.


### Making your changes



### Raising your Pull Request

More Coming Soon :)
