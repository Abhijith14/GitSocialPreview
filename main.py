from PIL import Image, ImageDraw, ImageFont
from scrape import scrape_basic_data
import scrape

bg = Image.open('assets/bg.png')
sign = Image.open('assets/signature.png')
face = Image.open('assets/face.png')
gitlogo = Image.open('assets/github.png')

git_contrib = Image.open('assets/git_contrib.png')
git_issues = Image.open('assets/git_issues.png')
git_stars = Image.open('assets/git_stars.png')
git_fork = Image.open('assets/git_fork.png')


lang_csharp = Image.open('assets/prog_lang/c#.png')
lang_cpp = Image.open('assets/prog_lang/c++.png')
lang_c = Image.open('assets/prog_lang/C.png')
lang_cmake = Image.open('assets/prog_lang/cmake.png')
lang_coffeescript = Image.open('assets/prog_lang/coffeescript.png')
lang_css = Image.open('assets/prog_lang/css.png')
lang_dart = Image.open('assets/prog_lang/dart.png')
lang_hack = Image.open('assets/prog_lang/hack.png')
lang_html = Image.open('assets/prog_lang/html.png')
lang_java = Image.open('assets/prog_lang/java.png')
lang_js = Image.open('assets/prog_lang/js.png')
lang_jupyter = Image.open('assets/prog_lang/jupyter.png')
lang_kotlin = Image.open('assets/prog_lang/kotlin.png')
lang_objc = Image.open('assets/prog_lang/obj-c.png')
lang_php = Image.open('assets/prog_lang/php.png')
lang_purescript = Image.open('assets/prog_lang/purescript.png')
lang_python = Image.open('assets/prog_lang/python.png')
lang_react = Image.open('assets/prog_lang/react.png')
lang_ruby = Image.open('assets/prog_lang/ruby.png')
lang_scss = Image.open('assets/prog_lang/scss.png')
lang_shell = Image.open('assets/prog_lang/shell.png')
lang_typescript = Image.open('assets/prog_lang/typescript.png')
lang_vb = Image.open('assets/prog_lang/vb.png')
lang_vue = Image.open('assets/prog_lang/vue.png')

img = bg.copy()


def add_git_ele():
    img.paste(git_contrib, (80, 490))
    img.paste(git_issues, (250, 490))
    img.paste(git_stars, (410, 490))
    img.paste(git_fork, (570, 490))


def add_basic_ele():
    img.paste(sign, (80, 50))
    img.paste(face, (900, 80))
    img.paste(gitlogo, (1100, 470))


def add_language(status, percentage, count, language):
    X, Y = 0, 0
    count = count * 100
    percent = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Montserrat-Medium.ttf', 23)

    if status:
        X, Y = 80 + count, 360
    else:
        X, Y = 80 + count, 320

    img.paste(language, (X, Y))
    percent.text((X, Y + 60), percentage, font=myFont, fill=(61, 67, 83))


def create_prog(prog, percent, down_stat):
    count = 0
    for i in range(len(prog)):
        print(prog[i] + " with " + percent[i])
        if prog[i] == "Python":
            add_language(down_stat, percent[i], count, lang_python)
        elif prog[i] == "CSS":
            add_language(down_stat, percent[i], count, lang_css)
        elif prog[i] == "HTML":
            add_language(down_stat, percent[i], count, lang_html)
        elif prog[i] == "JavaScript":
            add_language(down_stat, percent[i], count, lang_js)
        elif prog[i] == "Ruby":
            add_language(down_stat, percent[i], count, lang_ruby)
        elif prog[i] == "SCSS":
            add_language(down_stat, percent[i], count, lang_scss)
        elif prog[i] == "C#":
            add_language(down_stat, percent[i], count, lang_csharp)
        elif prog[i] == "Dart":
            add_language(down_stat, percent[i], count, lang_dart)
        elif prog[i] == "Java":
            add_language(down_stat, percent[i], count, lang_java)
        elif prog[i] == "C":
            add_language(down_stat, percent[i], count, lang_c)
        elif prog[i] == "C++":
            add_language(down_stat, percent[i], count, lang_cpp)
        elif prog[i] == "Kotlin":
            add_language(down_stat, percent[i], count, lang_kotlin)
        elif prog[i] == "Visual Basic .NET":
            add_language(down_stat, percent[i], count, lang_vb)
        elif prog[i] == "Jupyter Notebook":
            add_language(down_stat, percent[i], count, lang_jupyter)
        elif prog[i] == "PHP":
            add_language(down_stat, percent[i], count, lang_php)
        elif prog[i] == "Hack":
            add_language(down_stat, percent[i], count, lang_hack)
        elif prog[i] == "TypeScript":
            add_language(down_stat, percent[i], count, lang_typescript)
        elif prog[i] == "PureScript":
            add_language(down_stat, percent[i], count, lang_purescript)
        elif prog[i] == "Objective-C":
            add_language(down_stat, percent[i], count, lang_objc)
        elif prog[i] == "Shell":
            add_language(down_stat, percent[i], count, lang_shell)
        elif prog[i] == "CMake":
            add_language(down_stat, percent[i], count, lang_cmake)
        elif prog[i] == "CoffeeScript":
            add_language(down_stat, percent[i], count, lang_coffeescript)
        elif prog[i] == "Makefile":
            add_language(down_stat, percent[i], count, lang_cmake)
        count = count + 1



def add_repo_details(author_name, repo_name, desc_content, s_contrib, s_stars, s_forks, s_issues, s_lang, s_percent):
    X_repo, Y_repo, X_desc, Y_desc, down_stat = 0, 0, 0, 0, False
    author = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Montserrat-SemiBold.ttf', 60)
    author.text((80, 155), author_name + "/", font=myFont, fill=(61, 67, 83))

    repo = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Montserrat-ExtraBold.ttf', 60)

    if len(repo_name) <= 10:
        X_repo, Y_repo = 420, 155
    else:
        X_repo, Y_repo = 80, 215
        down_stat = True

    repo.text((X_repo, Y_repo), repo_name, font=myFont, fill=(61, 67, 83))

    desc = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Montserrat-Medium.ttf', 23)

    if down_stat:
        X_desc, Y_desc = 80, 305
    else:
        X_desc, Y_desc = 80, 245

    if len(desc_content) < 57:
        desc.text((X_desc, Y_desc), desc_content, font=myFont, fill=(61, 67, 83))
    else:
        down_stat = False

    add_repo_content(s_contrib, s_issues, s_stars, s_forks)

    create_prog(s_lang, s_percent, down_stat)


def add_repo_content(s_contrib, s_issues, s_stars, s_forks):
    contrib_no = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Trocchi-Regular.ttf', 35)
    contrib_no.text((130, 495), str(s_contrib), font=myFont, fill=(61, 67, 83))

    contrib = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Montserrat-Medium.ttf', 15)
    contrib.text((135, 540), "Contributors", font=myFont, fill=(61, 67, 83))


    issue_no = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Trocchi-Regular.ttf', 35)
    issue_no.text((300, 495), str(s_issues), font=myFont, fill=(61, 67, 83))

    issue = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Montserrat-Medium.ttf', 15)
    issue.text((305, 540), "Issues", font=myFont, fill=(61, 67, 83))


    star_no = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Trocchi-Regular.ttf', 35)
    star_no.text((460, 495), str(s_stars), font=myFont, fill=(61, 67, 83))

    star = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Montserrat-Medium.ttf', 15)
    star.text((465, 540), "Stars", font=myFont, fill=(61, 67, 83))


    fork_no = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Trocchi-Regular.ttf', 35)
    fork_no.text((610, 495), str(s_forks), font=myFont, fill=(61, 67, 83))

    fork = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Montserrat-Medium.ttf', 15)
    fork.text((615, 540), "Forks", font=myFont, fill=(61, 67, 83))
    # print(s_stars)

def start():
    add_basic_ele()
    add_git_ele()

    author_name, repo_name, s_desc, s_contrib, s_stars, s_forks, s_issues, s_lang, s_percent = scrape_basic_data()

    add_repo_details(author_name, repo_name, s_desc, s_contrib, s_stars, s_forks, s_issues, s_lang, s_percent)


def save():
    img.save('output/' + scrape.author + "-" + scrape.repo + '.png', quality=100)


start()
save()