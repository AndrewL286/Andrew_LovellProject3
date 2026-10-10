from nicegui import ui

spaceship = []
first_label = ui.label("Andrew Lovell")
first_label.classes("text-stone-900")
first_label.style("font-size: 200%")
drawing_surface = ui.interactive_image(size = (1000, 1240))
drawing_surface.classes("w-lg bg-sky-950")
nose_cone = """<polygon points= "375,200 475,25 575,200" fill="#A8A29E" />"""
main_body = """<rect x="375" y="200" width="200" height="600" fill="#A8A29E"/>"""
left_stabilizer = """<polygon points="375,800 250,800 375,600" fill="#A8A29E"/>"""
right_stabilizer = """<polygon points= "575,800 700,800 575,600" fill="#A8A29E"/>"""
#Lines 9-12 above are the main structure of the spaceship.
top_window1= """<circle cx="475" cy="300" r="50" fill="#212529" stroke="#212529" stroke-width="3"/>"""
middle_window2= """<circle cx="475" cy="500" r="50" fill="#212529" stroke="#212529" stroke-width="3"/>"""
bottom_window3= """<circle cx="475" cy="700" r="50" fill="#212529" stroke="#212529" stroke-width="3"/>"""
#Line 14-16 are for the windows of the spaceship.
line1 = f"""<line x1="375" y1="400" x2="575" y2="400" stroke="#212529" stroke-width=10 />"""
line2 = f"""<line x1="375" y1="600" x2="575" y2="600" stroke="#212529" stroke-width=10 />"""
#Lines 18 and 19 are lines that I used to section the rectangle(main body of the spaceship) into three pieces.
rocket_nozzle = """<polygon points= "425,800 400,950 550,950 525,800" fill="#212529"/>"""
fire1 = """<ellipse cx="475" cy="945" rx="72" ry="72" stroke="yellow" fill="yellow" stroke-width="3"/>"""
fire2 = """<polygon points= "400,950 475,1200 550,950" fill="red"/>"""
#Lines 21-23 are for the engine nozzle and the red and orange fire that is coming out of it.

spaceship.append(nose_cone)
spaceship.append(main_body)
spaceship.append(top_window1)
spaceship.append(middle_window2)
spaceship.append(bottom_window3)
spaceship.append(line1)
spaceship.append(line2)
spaceship.append(left_stabilizer)
spaceship.append(right_stabilizer)
spaceship.append(fire2)
spaceship.append(fire1)
spaceship.append(rocket_nozzle)
stuff_to_draw = "\n".join(spaceship)
drawing_surface.set_content(stuff_to_draw)

ui.run()