from app import create_app,db,User,Recipe
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db,'User': User, 'Recipe': Recipe}
    
if __name__ == '__main__':
    app.run(debug=True)