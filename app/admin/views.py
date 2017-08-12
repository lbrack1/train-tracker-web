from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import UserForm
from .. import db
from ..models import User

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

@admin.route('/users', methods=['GET', 'POST'])
@login_required
def list_users():
    """
    List all users
    """
    check_admin()

    users = User.query.all()

    return render_template('admin/users/users.html',
                           users=users, title="Users")

@admin.route('/users/add', methods=['GET', 'POST'])
@login_required
def add_user():
    """
    Add a user to the database
    """
    check_admin()

    add_users = True

    form = UserForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                                last_name=form.last_name.data,
                                email=form.email.data,
                                username = form.username.data,
                                password = form.password.data,
                                is_admin=form.is_admin.data,
                                is_blog=form.is_blog.data)
        try:
            # add user to the database
            db.session.add(user)
            db.session.commit()
            flash('You have successfully added a new user.')
        except:
            # in case user name already exists
            flash('Error: user already exists.')

        # redirect to user page
        return redirect(url_for('admin.list_users'))

    # load user template
    return render_template('admin/users/user.html', action="Add",
                           add_user=add_user, form=form,
                           title="Add User")

@admin.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    """
    Edit a user
    """
    check_admin()

    add_user = False

    user = User.query.get_or_404(id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.username = form.username.data
        user.is_admin = form.is_admin.data
        user.is_blog = form.is_blog.data
        db.session.commit()
        flash('You have successfully edited the user.')

        # redirect to the departments page
        return redirect(url_for('admin.list_users'))

    form.first_name.data = user.first_name
    form.last_name.data = user.last_name
    form.email.data = user.email
    form.username.data = user.username
#    form.password.data = user.password
    form.is_admin.data = user.is_admin
    form.is_blog.data = user.is_blog
    return render_template('admin/users/user.html', action="Edit",
                           add_user=add_user, form=form,
                           user=user, title="Edit User")

@admin.route('/users/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    """
    Delete a user from the database
    """
    check_admin()

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('You have successfully deleted the user.')

    # redirect to the users page
    return redirect(url_for('admin.list_users'))

    return render_template(title="Delete User")
