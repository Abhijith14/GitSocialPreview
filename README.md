<h1 align="center">
  Social Preview Autogenerator
</h1>
<p align="center">
  An autogenerator for your repo social preview
</p>

![demo](https://raw.githubusercontent.com/Abhijith14/GitSocialPreview/master/assets/sample.png)

<br>
<br>


## 📕 Installation

### 🕷️ Create an environment
Whatever you prefer (e.g. `conda` or `venv`)
```console
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

### 🕷️ Activate the venv folder
Windows:
```console
venv\Scripts\activate
```
Mac / Linux (Create a venv, activate it and install requirements.txt):
```console
. python3 -m venv venv
. venv/bin/activate
```

### 🕷️ Install Dependencies

Install Dependencies only for Mac/Linux:
 ```console
. pip install -r requirements.txt
 ```


## ⚙️ Customize the preview
Inside [assets](assets/) folder you have, 
#                          |  Image                    | Size (width x height)
:-------------------------:|:-------------------------:|:-------------------------:
Background         |  ![bg](https://raw.githubusercontent.com/Abhijith14/GitSocialPreview/master/assets/bg.png)        | 1280 x 640 px
Face               |  ![face](https://raw.githubusercontent.com/Abhijith14/GitSocialPreview/master/assets/face.png)    | 300 x 300 px
Signature          |  ![Signature](https://raw.githubusercontent.com/Abhijith14/GitSocialPreview/master/assets/signature.png)   | 250 x 65 px
Contributors Icon  |  ![Contributors](https://raw.githubusercontent.com/Abhijith14/GitSocialPreview/master/assets/git_contrib.png) | 40 x 40 px
Forks Icon         |  ![Forks](https://raw.githubusercontent.com/Abhijith14/GitSocialPreview/master/assets/git_fork.png)  | 40 x 40 px
Issues Icon        |  ![Issues](https://raw.githubusercontent.com/Abhijith14/GitSocialPreview/master/assets/git_issues.png)  | 40 x 40 px
Stars Icon         |  ![Stars](https://raw.githubusercontent.com/Abhijith14/GitSocialPreview/master/assets/git_stars.png)  | 40 x 40 px
Github Icon        |  ![Github](https://raw.githubusercontent.com/Abhijith14/GitSocialPreview/master/assets/github.png)  | 100 x 100 px

You can change the images according to your usage. Remember to `KEEP THE SAME SIZE` as of the image you are replacing.

## 👨‍💻 Usage

Find the link of your repo. Paste it inside `url` variable inside [scripts.py](scripts.py) file.

```console
url = "https://github.com/Abhijith14/GitSocialPreview"
```

Run
```console
python main.py
```

This will start creating the preview.<br>
You can find your results inside [output](output/) folder as : `gitusername/reponame`<br>
Eg : `Abhijith14/GitSocialPreview`
<br>


### 🛠️ Built With

* [Python 3.7](https://www.python.org/) - Creating Project


### ❤️ Authors

* **Abhijith Udayakumar** - *Design & Development* - [Abhijith14](https://github.com/Abhijith14)

<br>
<br>

## 🚨 Forking this repo (please read!)

_**yes, with attribution**_.

I value keeping my work open source, but as you all know, _**plagiarism is bad**_. It's always disheartening whenever I find that someone has copied my work without giving me credit. I spent a non-trivial amount of effort building and designing this project, and I am proud of it! All I ask of you all is to not claim this effort as your own.


### TL;DR

Yes, you can fork this repo. Please give me proper credit by linking back to [Abhijith14/GitSocialPreview](https://github.com/Abhijith14/GitSocialPreview). Thanks!