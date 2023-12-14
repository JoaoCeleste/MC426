from models.database import db
from models.recipe import Recipe
from flask import request, url_for, redirect
from forms.comment_form import CommentForm
from models.comment import Comment
from facade.user_facade import UserFacade

user_facade = UserFacade()

def create(id):
    recipe = Recipe.query.get(id)
    if not user_facade.is_authenticated():
        return redirect(url_for('routes.recipe_show', id=recipe.id))

    form = CommentForm(request.form)

    if form.validate_on_submit():
        comment = Comment(text=form.comment.data, recipe_id=recipe.id, user=user_facade.current_user())
        print(comment)
        db.session.add(comment)
        db.session.commit()

    return redirect(url_for('routes.recipe_show', id=recipe.id))
