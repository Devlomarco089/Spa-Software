from components.home import home_view
from components.register_view import register_view
from components.login_view import login_view
from components.services_view import services_view
from components.user_panel import user_panel
from components.professional_panel import professional_panel
from components.professional_register import professional_register_view

def route_change(page, route):
    page.clean()
    if page.route == "/register":
        register_view(page)
    elif page.route == "/login":
        login_view(page)
    elif page.route == "/services":
        services_view(page)
    elif page.route == "/profile":
        user_panel(page)
    elif page.route == "/professional":
        professional_panel(page)
    elif page.route == "/professional-register":
        professional_register_view(page)
    else:
        home_view(page)
