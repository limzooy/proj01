#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'paas', #2
        'USER': 'root', #3                      
        'PASSWORD': 'root',  #4              
        # 'HOST': '192.168.0.18',   #5 
        'HOST': 'localhost',                
        'PORT': '3306', #6
    }
}
SECRET_KEY ='django-insecure-kcvci_!l2()nsc+d8fpxoh@#va%-8n8%oe%sj!_t6mty3bbyx^'