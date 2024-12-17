from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from docx import Document
from docx.shared import RGBColor
from django.conf import settings
import os
from .forms import FileForm
from .models import File
from bias_checker.static.bias_checker.dictionary import dictionary
import re
from django.contrib import messages
# Create your views here.

def index(request):
    try:    
        if request.method == "POST":
            form = FileForm(request.POST, request.FILES)
            context = {'form' : form}
            if form.is_valid():
                form.save()
            else:
                return render(request, "bias_checker/error.html", {"content":"FILE ALREADY EXISTS"})

            count = 0
            gender = dictionary
            last = File.objects.last()

            save_directory = os.path.join(settings.BASE_DIR, 'media')
            file_path = os.path.join(save_directory,str(last.file))#Get the saved file from submit
            doc = Document(file_path)
            for p in doc.paragraphs:
                original_text = p.text
                parts = original_text.split(" ")
                p.clear()
                for part in parts:
                    #cleaned_data = re.sub(r"’s", '', part)
                    #cleaned_data1 = re.sub(r"[^A-Za-z0-9.-]", '', cleaned_data)
                    styled_run = p.add_run(part + " ")
                    for word in gender:
                        isMatch = re.match(rf"\b{word}\b", part)
                        if isMatch:
                            count = count + 1
                            styled_run.font.color.rgb = RGBColor(255,0,0)

                    # if cleaned_data1.lower() in gender:
                    #     count = count + 1
                    #     styled_run = p.add_run(part + " ")
                    #     styled_run.font.color.rgb = RGBColor(255,0,0)
                    # else:
                    #     p.add_run(part + " ")

            report = ["No gender-bias detected", f"{count} gender-bias detected"]
            if(count > 0):
                doc.add_paragraph(report[1])
            else:
                doc.add_paragraph(report[0])
            print(count)
            fileName = f"gender_checked_{last.id}_{last.file}"
            File.objects.filter(pk = last.id).update(file = fileName)# update the database to match the file
            doc.save(os.path.join(save_directory,fileName)) #save the file with a new filename
            os.remove(file_path) #remove the old file
            messages.add_message(request,messages.INFO, "File submitted. Click 'Files' button to view the output.")
        else:
            form = FileForm
            context = {'form' : form}
        return render(request, 'bias_checker/index.html', context)
    except:
        print("error in input")
        return render(request, 'bias_checker/error.html', {"content": "INTERNAL ERROR"})
    #return render(request, 'bias_checker/index.html', context)
    

def output(request):
    try:
        if request.method == "POST":
            file_id = request.POST.get("data-id")
            print(file_id)
            data = File.objects.filter(pk = file_id).first()
            print(data)
            save_directory = os.path.join(settings.BASE_DIR, 'media')
            file_path = os.path.join(save_directory, str(data.file))#Get the saved file from submit

            print(file_path)
            os.remove(file_path)
            data.delete()
            messages.add_message(request,messages.INFO, "File deleted")
            return redirect(reverse("bias_checker:output"))
        else:

            form = File.objects.all()
            context = {'form': form}
            #print(form)
            if not form.exists():
                print("Empty query")
                return render(request, "bias_checker/output.html", {"content": "No data"})

            return render(request, "bias_checker/output.html", context)
    except:
        print("error in output")
        return render(request, "bias_checker/error.html", {"content":"INTERNAL ERROR"})
    
def convert(request):
    try:
        if request.method == "POST":
            data:str = request.POST.get("hiddenTextArea")
            #cleaned_data = data.replace('</div>', "").replace('<span class="highlight-word">', "").replace('</span>',"")
            separated = data.split("<div>")
            print(separated)

            #create empty file
            File.objects.create(file = "generated_file.docx")
            last = File.objects.last()
            doc = Document()
            
            for row in separated:
                doc.add_paragraph(row)

            fileName = f"{last.id}_{last.file}"
            File.objects.filter(pk = last.id).update(file = fileName)# update the database to match the file
            save_directory = os.path.join(settings.BASE_DIR, 'media')
            file_path = os.path.join(save_directory, fileName)#Get the saved file from submit
            doc.save(file_path)
            #return redirect(reverse("bias_checker:index"))
            messages.add_message(request,messages.INFO, "File generated. Click 'Files' button to view the output.")
        return redirect(reverse("bias_checker:index"))
        return render(request, "bias_checker/index.html", {"success":"File generated is located at 'Files'"})
    except:
        return render(request, "bias_checker/error.html", {"content":"CONVERSION ERROR"})


# def error(request):
#     return render(request, "bias_checker/error.html", {"content":"Error in error"})