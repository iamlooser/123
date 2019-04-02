from django.shortcuts import render, redirect
import pyrebase
from django.contrib import auth
from django.contrib.auth.decorators import login_required
config = {
    'apiKey': "AIzaSyC4pzPtiIhmYbnwlhVc9ne41gCHLla8wTk",
    'authDomain': "zest-2k19-37078.firebaseapp.com",
    'databaseURL': "https://zest-2k19-37078.firebaseio.com",
    'projectId': "zest-2k19-37078",
    'storageBucket': "zest-2k19-37078.appspot.com",
    'messagingSenderId': "712754236483"
    }

firebase = pyrebase.initialize_app(config)
authentication = firebase.auth()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('zest-2k19-37078-firebase-adminsdk-2z2uu-fda1eb5560.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def home(request):
    try:
        user = request.session['uid']
        user_info = authentication.get_account_info(user)
        user_id = user_info['users'][0]['localId']
        user_data = db.collection(u'users').document(user_id).get()
        user_data = user_data.to_dict()
        args = {
            'user_id':user_id,
            'user_name':user_data['name'],
            'user':user_data,
            }
        return render(request, 'project/home.html', args )
    except:
        return render(request, 'project/home.html')

def sign_in(request):
    try:
        user = request.session['uid']
        user_info = authentication.get_account_info(user)
        user_id = user_info['users'][0]['localId']
        return render(request, 'project/home.html', {'user_id':user_id})
    except:
        return render(request, 'project/sign_in.html')

def signed_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = authentication.sign_in_with_email_and_password(email, password)
        user_id = str(user['idToken'])
        session_id = str(user['idToken'])
        request.session['uid']=str(session_id)

        return redirect("/")
    except:
        message="Invalid Credentails. Plz SignIn with correct Info"
        return render(request, 'project/sign_in.html', {'msg':message})

def sign_up(request):
    return render(request, 'project/sign_up.html')

def signed_up(request):
    try:
        user = request.session['uid']
        user_info = authentication.get_account_info(user)
        user_id = user_info['users'][0]['localId']
        return render(request, 'project/home.html', {'user_id':user_id})
    except:
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user =authentication.create_user_with_email_and_password(email, password)
            uid = str(user['localId'])
            doc_ref = db.collection(u'users').document(uid)
            doc_ref.set({
                u'name': name,
                u'email': email,
                u'status': u'0',
                u'committee': u'None',

            })
            return render(request, 'project/sign_in.html')
        except:
            message = "INVALID_EMAIL or INVALID_PASSWORD"
            return render(request, 'project/sign_up.html', {'msg':message})

def logout(request):
    auth.logout(request)
    return redirect("/")

def reset_password(request):
    return render(request, 'project/reset_password.html')

def reset_password_send(request):
    email = request.POST.get('email')
    try:
        authentication.send_password_reset_email(email)
        message ="Reset password link will send to your MAIL"
        return render(request, "project/sign_in.html", {'msg':message})
    except:
        message ="Enter the VALDID Email"
        return render(request, "project/reset_password.html", {'msg':message})

def profile(request):
    try:
        user = request.session['uid']
        user_info = authentication.get_account_info(user)
        user_id = user_info['users'][0]['localId']
        user_data = db.collection(u'users').document(user_id).get()
        user_data = user_data.to_dict()
        args = {
            'user_id':user_id,
            'user_name':user_data['name'],
            'user':user_data,
            }
        return render(request, 'project/profile.html', args )
    except:
        return redirect('/sign-in')
