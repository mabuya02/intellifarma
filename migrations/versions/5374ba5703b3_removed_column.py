"""removed column

Revision ID: 5374ba5703b3
Revises: 07564a8584bf
Create Date: 2023-11-25 19:42:37.933927

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5374ba5703b3'
down_revision = '07564a8584bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('activation_code')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activation_code', mysql.VARCHAR(length=6), nullable=True))

    # ### end Alembic commands ###
