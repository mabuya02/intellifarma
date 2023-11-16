""" Updated soil parameter table

Revision ID: 257f9a9b4284
Revises: 6255d7504f3e
Create Date: 2023-11-16 11:26:23.100157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '257f9a9b4284'
down_revision = '6255d7504f3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('soil_parameters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('soil_parameters', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
