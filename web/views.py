from django.shortcuts import render
from django.http import *
from . import models
# Create your views here.
import random

def index(request):
    return render(request, "web/main.html")

def rules(request):
    return render(request, "web/rules.html")

def contact(request):
    return render(request, "web/contact.html")

def thanks(request):
    return render(request, "web/thanks.html")

def p_reg(request):
    if request.method == "GET":
        return render(request, "web/part_reg.html")
    else:
        name = request.POST["name"]
        email = request.POST["email"]
        ph = str(request.POST["ph"])
        team = request.POST["team"]
        teams = models.teams.objects.all()
        team_exists = False
        not_full = False
        num_of_part = 0
        for x in teams:
            if int(team) == int(x.teamID):
                team_exists = True
                if x.team_type == "Forensic":
                    num_of_part = models.participants.objects.filter(team=x.teamID)
                    if len(num_of_part) < 2:
                        not_full = True
                        break
                    else:
                        break    
                else:
                    num_of_part = models.participants.objects.filter(team=x.teamID)
                    if len(num_of_part) < 4:
                        not_full = True
                    else:
                        break 
                    
                

        if team_exists == False:
            return render(request, "web/part_reg.html", {
                "message":"The team entered does not exist"
            }) 
        elif not_full == False:
            return render(request, "web/part_reg.html", {
                "message":"The team entered is full"
            })       
        else:
            p = models.participants(name=name,email=email, phone_number=ph, team=team)
            p.save()
            return HttpResponseRedirect('/thanks')

def t_reg(request):
    if request.method == "GET":
        return render(request, "web/team_reg.html")
    else:
        name = request.POST["name"]
        email = request.POST["email"]
        ph = str(request.POST["ph"])
        team_name = request.POST["team_name"]
        team_type = request.POST["team_type"]
        teamid = random.randint(1,1000000)
        teams = models.teams.objects.all()
        for x in teams:
            if x.teamID == teamid:
                teamid = random.randint(1,1000000)

        t = models.teams(teamID=teamid, leader_name=name, leader_email=email, leader_phone_number=ph, team_name=team_name, points = 0, team_type=team_type)
        t.save()
        return HttpResponseRedirect("/thanks")


def lad(request):
    if request.method == "GET":
        trivial_loe = models.leaderboard.objects.filter(name="Trivial")
        forensic_loe = models.leaderboard.objects.filter(name="Forensic")
        FLOE = 0
        LOE = 0
        trivial = models.teams.objects.filter(team_type="Trivial")
        Forensic = models.teams.objects.filter(team_type="Forensic")
        for vd in trivial_loe:
            LOE = vd.level
        for f in forensic_loe:
            FLOE = f.level    
        return render(request, "web/leaderboard.html", {
            "trivial":trivial,
            "Forensic":Forensic,
            "LOE":LOE,
            "FLOE":FLOE
        })
        
            

