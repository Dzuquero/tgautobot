from alembic import op
import sqlalchemy as sa
revision = "0001"
down_revision = None
def upgrade():
    op.create_table(
        "cars",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("brand", sa.String()),
        sa.Column("model", sa.String()),
        sa.Column("year", sa.Integer()),
        sa.Column("price", sa.Float()),
        sa.Column("color", sa.String()),
        sa.Column("url", sa.String(), unique=True),
    )
def downgrade():
    op.drop_table("cars")
