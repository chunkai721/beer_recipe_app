from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from flask_babel import _
from beer_recipe_app import app, db, bcrypt
from beer_recipe_app.forms import RegistrationForm, LoginForm, RecipeForm
from beer_recipe_app.models import User, Recipe

@app.route("/")
@app.route("/home")
def home():
    recipes = Recipe.query.all()
    return render_template('home.html', recipes=recipes)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(_('Your account has been created! You are now able to log in'), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(_('Login Unsuccessful. Please check username and password'), 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/recipe/new", methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(name=form.name.data, ingredients=form.ingredients.data, cost=form.cost.data, author=current_user)
        db.session.add(recipe)
        db.session.commit()
        flash(_('Your recipe has been created!'), 'success')
        return redirect(url_for('home'))
    return render_template('create_recipe.html', title='New Recipe', form=form, legend='New Recipe')

@app.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html', title=recipe.name, recipe=recipe)

@app.route("/recipe/<int:recipe_id>/update", methods=['GET', 'POST'])
@login_required
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        abort(403)
    form = RecipeForm()
    if form.validate_on_submit():
        recipe.name = form.name.data
        recipe.ingredients = form.ingredients.data
        recipe.cost = form.cost.data
        db.session.commit()
        flash(_('Your recipe has been updated!'), 'success')
        return redirect(url_for('recipe', recipe_id=recipe.id))
    elif request.method == 'GET':
        form.name.data = recipe.name
        form.ingredients.data = recipe.ingredients
        form.cost.data = recipe.cost
    return render_template('create_recipe.html', title='Update Recipe', form=form, legend='Update Recipe')

@app.route("/recipe/<int:recipe_id>/delete", methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        abort(403)
    db.session.delete(recipe)
    db.session.commit()
    flash(_('Your recipe has been deleted!'), 'success')
    return redirect(url_for('home'))
