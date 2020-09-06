from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///todo.db'
db = SQLAlchemy(app)


# Defining data
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<<Todo {self.id}: {self.description}>>'


db.create_all()


@app.route('/')
def index():
    homepage = render_template('index.html', items=Todo.query.all())

    return homepage

@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.form.get('description', '')  # Retrieve data from form input (based on input name)
    todo = Todo(description=description)  # Instantiate the object (record) with the appropriate value

    # To the current session, add the records to the table and commit (to save)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))  # specific handler/function name


if __name__ == '__main__':
    app.run(debug=True)
