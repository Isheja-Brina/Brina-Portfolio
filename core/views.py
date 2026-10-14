from django.shortcuts import render


def index(request):
    # Display the home page
    return render(request, 'core/index.html')


def about(request):
    # Display information about the library and its creator.
    return render(request, 'core/about.html')


def contact(request):
    # Display the contact form and handle its submission.
    success = False

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        # Check that all required fields contain text.
        if name and email and message:
            success = True

    return render(request, 'core/contact.html', {
        'success': success
    })