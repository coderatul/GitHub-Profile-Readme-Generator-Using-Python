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
print("❀ If you don't want to fill something then just leave it blank & press enter ❀")

# inputting name
print('Title')
Name = input("Hi 👋+ I'm 🠮 ")
name = ('<h1 align=\"center\">Hi 👋 I\'m'+" "+ Name + '</h1>')

# inputting subtitle
sub = input("Enter Subtitle 🠮")
subtitle = ('<h3 align="center">'+ sub+ '</h3>')

# inputting github user name
user_name = input("Just Enter your github user name (eg: coderatul) :")
git = ('<p align="left"> <img src="https://komarev.com/ghpvc/?username='+user_name+'&label=Profile%20views&color=0e75b6'
       '&style=flat"alt='+'""'+user_name+'""'"/></p>")

trophy = ('<p align=\"left\"> <a href="https://github.com/ryo-ma/github-profile-trophy"><img '
          'src="https://github-profile-trophy.vercel.app/?username='+ user_name+'"'+ ""+ 'alt='+'""'+user_name+'""'+
          " /></a> </p>")
print("Work")

# inputting name of project in which user is currently working
project_name = input('🔭 I’m currently working on 🠮')

# inputting link of the project in which user is currently working
project_link = input('Link to above mentioned project 🠮 ')
current_project = ('- 🔭 I’m currently working on '+ '['+ project_name+ ']'+ '('+ project_link+ ')')

# inputting what what user is learning
learn = input("🌱 I’m currently learning (If more than one separate Them with commas eg:seo+python) 🠮")
current_learn = ('- 🌱 I’m currently learning '+ ""+ '**'+ learn+ '**')

# inputting project info for which user is using seeking collaborating
collaborate_project = input("👯 I’m looking to collaborate on 🠮")

# inputting project link for which user is seeking collaboration
collaborate_project_link = input("Link to above mentioned project 🠮")
collaborate = ('- 👯 I’m looking to collaborate on '+ '['+ collaborate_project+ ']'+ '('+ collaborate_project_link+ ')')

# inputting project info in which user is seeking
help_txt = input("🤝 I’m looking for help with 🠮")
Help = ('- 🤝 I’m looking for help with '+ ""+ '**'+ help_txt+ '**')

# inputting link to portfolio
portfolio_link = input("👨‍ 💻 All of my projects are available at (link to portfolio) 🠮")
all_my_project = ('- 👨 ‍💻 All of my projects are available at '+ '['+ portfolio_link+ ']'+ '('+ portfolio_link+ ')')

# inputting link to blog
blog_link = input("📝 I regularly write articles on 🠮")
blog = ('- 📝 I regularly write articles on '+ '['+ blog_link+ ']'+ '('+ blog_link+ ')')

# inputting what what technology user knows
ask_me_about_topic = input("💬 Ask me about 🠮")
ask_me_about = ('- 💬 Ask me about '+'**'+ask_me_about_topic+'**')

# inputting email Id
email_id = input("📫 How to reach me 🠮")
email = ('- 📫 How to reach me '+ ""+ ""+ '**'+ email_id+ '**')

# inputting link to resume
resume_link = input("📄 Know about my experiences (link to resume) 🠮")
resume = ("- 📄 Know about my experiences "+ ""+ "["+ resume_link+ "]"+ "("+ resume_link+ ")")

# inputting fun fact
fun_fact = input("⚡ Fun fact 🠮")
Fun_fact = ("- ⚡ Fun fact "+"**"+fun_fact+"**")

most_used_language = ('<p><img align="left" src="https://github-readme-stats.vercel.app/api/top-langs?username='
    + user_name+ '&show_icons=true&locale=en&layout=compact" alt='+'""'+user_name+'""'+ "/></p>")

# printing statistics
full_statistics = ('<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username='+ user_name+
                   '&show_icons=true&locale=en\"'+ "alt="+'""'+user_name+'""'+ "/></p>")

# printing streaks
streak = ('<p><img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user='+ user_name+ '&\" alt='+
          '""'+user_name+'""'+ "/></p")

#printing output
if len(Name)!= 0 : print(name)
print()
if len(sub)!= 0 : print(subtitle)
print()
if len(user_name)!= 0 : print(git)
print()
if len(user_name)!= 0 : print(trophy)
print()
if len(project_name)!= 0 : print(current_project)
print()
if len(learn)!= 0 : print(current_learn)
print()
if len(collaborate_project)!= 0 : print(collaborate)
print()
if len(help_txt)!= 0 : print(Help)
print()
if len(portfolio_link)!= 0 : print(all_my_project)
print()
if len(blog_link)!= 0 : print(blog)
print()
if len(ask_me_about_topic)!= 0 : print(ask_me_about)
print()
if len(email_id)!= 0 : print(email)
print()
if len(resume_link)!= 0 : print(resume)
print()
if len(fun_fact)!= 0 : print(Fun_fact)
print()
if len(user_name)!= 0 : print(most_used_language)
print()
if len(user_name)!= 0 : print(full_statistics)
print()
if len(user_name)!= 0 : print(streak)
