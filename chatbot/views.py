from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import google.generativeai as genai

@login_required
def chatbot_view(request):
    response = None
    
    if request.method == 'POST':
        user_message = request.POST.get('message')
        
        if user_message:
            try:
                
                genai.configure(api_key=settings.GEMINI_API_KEY)
                
            
                model = genai.GenerativeModel('gemini-2.5-pro')
                
                
                prompt = f"""You are a helpful hospital assistant for HealthZone HMS. 
                Answer the following question professionally and concisely:
                
                Question: {user_message}
                
                Remember: You are a medical assistant. Give general health advice only.
                For emergencies, advise users to visit the hospital immediately."""
                
                # Get response from Gemini
                chat_response = model.generate_content(prompt)
                response = chat_response.text
                
            except Exception as e:
                response = f"Sorry, I'm having trouble responding. Error: {str(e)}"
                messages.error(request, "AI service error. Please try again.")
    
    return render(request, 'chatbot/chatbot.html', {'response': response})
