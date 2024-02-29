from wake_net.main import create_app, db
from wake_net.models import Device

app = create_app()


@app.shell_context_processor
def make_shell_contexts():
    return dict(app=app, db=db, Device=Device)
