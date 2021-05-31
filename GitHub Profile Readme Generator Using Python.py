# printing banner
print('''            
 ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗     ██████╗ ███████╗ █████╗ ██████╗ ███╗   ███╗███████╗    
██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝    
██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝    ██████╔╝█████╗  ███████║██║  ██║██╔████╔██║█████╗      
██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗    ██╔══██╗██╔══╝  ██╔══██║██║  ██║██║╚██╔╝██║██╔══╝      
╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝    ██║  ██║███████╗██║  ██║██████╔╝██║ ╚═╝ ██║███████╗    
 ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚══════╝    

                 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗             
                ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗            
                ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝            
                ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗            
                ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║            
                 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝            

      ''')
# printing name of Author
print('Author : coderatul')
print("❀ If you don\'t want to fill something then just leave it blank & press enter ❀")

# inputting name
print('Title')
Name = input("Hi 👋, I'm 🠮 ")
name = ['<h1 align=\"center\">Hi 👋, I\'m', " ", Name, '</h1>']

# inputting subtitle
sub = input("Enter Subtitle 🠮")
subtitle = ['<h3 align="center">', sub, '</h3>']

# inputting github user name
user_name = input("just Enter your github user name (eg: coderatul) :")

# inputting github user with 2 double quotes "" for displaying profile visits , trophy
git_user = input("Enter your github username with double-quotes (eg:\"coderatul\") 🠮")

# inputting github user name with double quotes at ending for displaying profile visits , trophy
git_user_trophy = input("Enter your github username with double-quotes at end (eg:coderatul\") 🠮")
git = ['<p align="left"> <img src="https://komarev.com/ghpvc/?username=coderatul&label=Profile%20views&color=0e75b6'
       '&style=flat"alt=', git_user, "/></p>"]
trophy = ['<p align=\"left\"> <a href="https://github.com/ryo-ma/github-profile-trophy"><img '
          'src="https://github-profile-trophy.vercel.app/?username=', git_user_trophy, "", 'alt=', git_user,
          " /></a> </p>"]
print("work")

# inputting name of project in which user is currently working
project_name = input('🔭 I’m currently working on 🠮')

# inputting link of the project in which user is currently working
project_link = input('Link to above mentioned project 🠮 ')
current_project = ['- 🔭 I’m currently working on ', '[', project_name, ']', '(', project_link, ')']

# inputting what what user is learning
learn = input("🌱 I’m currently learning (if more than one separate Them with commas eg:seo,python) 🠮")
current_learn = ['- 🌱 I’m currently learning ', "", '**', learn, '**']

# inputting project info for which user is using seeking collaborating
collaborate_project = input("👯 I’m looking to collaborate on 🠮")

# inputting project link for which user is seeking collaboration
collaborate_project_link = input("Link to above mentioned project 🠮")
collaborate = ['- 👯 I’m looking to collaborate on ', '[', collaborate_project, ']', '(', collaborate_project_link, ')']

# inputting project info in which user is seeking
help_txt = input("🤝 I’m looking for help with 🠮")
Help = ['- 🤝 I’m looking for help with ', "", '**', help_txt, '**']

# inputting link to portfolio
portfolio_link = input("👨‍ 💻 All of my projects are available at (link to portfolio) 🠮")
all_my_project = ['- 👨 ‍💻 All of my projects are available at ', '[', portfolio_link, ']', '(', portfolio_link, ')']

# inputting link to blog
blog_link = input("📝 I regularly write articles on 🠮")
blog = ['- 📝 I regularly write articles on ', '[', blog_link, ']', '(', blog_link, ')']

# inputting what what technology user knows
ask_me_about_topic = input("💬 Ask me about 🠮")
ask_me_about = ['- 💬 Ask me about ','**',ask_me_about_topic,'**']

# inputting email Id
email_id = input("📫 How to reach me 🠮")
email = ['- 📫 How to reach me ', "", "", '**', email_id, '**']

# inputting link to resume
resume_link = input("📄 Know about my experiences (link to resume) 🠮")
resume = ["- 📄 Know about my experiences ", "", "[", resume_link, "]", "(", resume_link, ")"]

# inputting fun fact
fun_fact = input("⚡ Fun fact 🠮")
Fun_fact = ["- ⚡ Fun fact ","**",fun_fact,"**"]

most_used_language = ['<p><img align="left" src="https://github-readme-stats.vercel.app/api/top-langs?username='
    , user_name, '&show_icons=true&locale=en&layout=compact" alt=', git_user, "/></p>"]

# printing statistics
full_statistics = ['<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=', user_name,
                   '&show_icons=true&locale=en\"', "alt=", git_user, "/></p>"]

# printing streaks
streak = ['<p><img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=', user_name, '&\" alt=',
          git_user, "/></p"]

# printing results

# printing user name
if len(Name) == 0:
    pass
else:
    for A in name:
        print(A, end="")
print()

# printing subtitle
if len(sub) == 0:
    pass
else:
    for t in subtitle:
        print(t, end="")
print()

# printing github profile visit's
if len(git) == 0:
    pass
else:
    for u in git:
        print(u, end="")
print()

# printing github trophy
for l in trophy:
    print(l, end="")
print()
print()

# printing project in which user is currently working
if len(project_name or project_link) == 0:
    pass
else:
    for d in current_project:
        print(d, end='')
print()

# printing what what user is learning
if len(learn) == 0:
    pass
else:
    for e in current_learn:
        print(e, end="")
print()
print()

# printing project in which user is seeking collaboration
if len(collaborate_project or collaborate_project_link) == 0:
    pass
else:
    for v in collaborate:
        print(v, end="")
print()
print()

# printing project for which user is seeking help
if len(help_txt) == 0:
    pass
else:
    for a in Help:
        print(a, end="")
print()
print()

# printing link to portfolio
if len(portfolio_link) == 0:
    pass
else:
    for p in all_my_project:
        print(p, end="")
print()

# printing link to blog
if len(blog_link) == 0:
    pass
else:
    for r in blog:
        print(r, end="")
print()

# printing what what technologies user knows
if len(ask_me_about_topic) == 0:
    pass
else:
    for i in ask_me_about:
        print(i, end="")
print()

# printing email Id of user
if len(email_id) == 0:
    pass
else:
    for y in email:
        print(y, end="")
print()

# printing link to resume
if len(resume_link) == 0:
    pass
else:
    for aka in resume:
        print(aka, end="")
print()

# printing fun fact
if len(fun_fact) == 0:
    pass
else:
    for r in Fun_fact:
        print(r, end="")
print()

# printing most used language
for t in most_used_language:
    print(t, end='')
print()

# printing statistics
for h in full_statistics:
    print(h, end="")
print()

# printing streaks
for u in streak:
    print(u, end="")
