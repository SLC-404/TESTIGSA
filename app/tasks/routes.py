from flask import flash, redirect, render_template, request, url_for

from app.extensions import db
from app.models import STATUSES, Task
from app.tasks import bp
from app.tasks.forms import TaskForm


@bp.get("/")
def index():
    q = request.args.get("q", "").strip()
    status = request.args.get("status", "")

    stmt = db.select(Task).order_by(Task.created_at.desc(), Task.id.desc())
    if q:
        stmt = stmt.where(Task.title.ilike(f"%{q}%"))
    if status in STATUSES:
        stmt = stmt.where(Task.status == status)

    pagination = db.paginate(stmt, per_page=10, error_out=False)
    return render_template("tasks/index.html", pagination=pagination, q=q, status=status,
                           statuses=STATUSES)


@bp.route("/create", methods=["GET", "POST"])
def create():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data.strip(),
                    description=form.description.data or None,
                    status=form.status.data)
        db.session.add(task)
        db.session.commit()
        flash("Tarea creada", "success")
        return redirect(url_for("tasks.index"))
    return render_template("tasks/form.html", form=form, title="Nueva tarea")


@bp.route("/<int:task_id>/update", methods=["GET", "POST"])
def update(task_id):
    task = db.get_or_404(Task, task_id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data.strip()
        task.description = form.description.data or None
        task.status = form.status.data
        db.session.commit()
        flash("Tarea actualizada", "success")
        return redirect(url_for("tasks.index"))
    return render_template("tasks/form.html", form=form, title="Editar tarea")


@bp.post("/<int:task_id>/delete")
def delete(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Tarea eliminada", "warning")
    return redirect(url_for("tasks.index"))
