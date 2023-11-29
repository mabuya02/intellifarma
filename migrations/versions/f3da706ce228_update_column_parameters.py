"""Update column parameters

Revision ID: f3da706ce228
Revises: d4c70617c6dc
Create Date: 2023-11-26 11:05:23.109872

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f3da706ce228'
down_revision = 'd4c70617c6dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('activation_code',
               existing_type=mysql.VARCHAR(length=6),
               type_=sa.String(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('activation_code',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=6),
               existing_nullable=True)

    # ### end Alembic commands ###