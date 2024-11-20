from uuid import uuid4
import random

from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.db import Session, Tour


tour_blueprint = Blueprint("tours", __name__)


@tour_blueprint.get("/")
def index():
    with Session() as session:
        tours = session.query(Tour).where(Tour.is_reserved == False).all()
        random.shuffle(tours)
        return render_template("index.html", tours=tours)


@tour_blueprint.route("/add_tour/", methods=["POST", "GET"])
def add_tour():
    if request.method == "POST":
        with Session() as session:
            number = request.form.get("number")
            name = request.form.get("name")

            tour = Tour(
                number=number,
                name=name,)
            session.add(tour)
            session.commit()
            return redirect(url_for("tours.index"))

    return render_template("reserve_tour.html")


@tour_blueprint.get("/reserve/<int:id>")
def reserve(id):
    with Session() as session:
        tour = session.query(Tour).where(Tour.id == id).first()
        tour.is_reserved = True
        session.commit()
        return render_template("reserved.html", tour=tour)


@tour_blueprint.get("/manage-tours/")
def manage_tours():
    with Session() as session:
        tours = session.query(Tour).all()
        return render_template("manage_tours.html", tours=tours)


@tour_blueprint.get("/del/<int:id>")
def del_tour(id):
    with Session() as session:
        tour = session.query(Tour).where(Tour.id == id).first()
        session.delete(tour)
        session.commit()
        return redirect(url_for("tours.manage_tours"))


