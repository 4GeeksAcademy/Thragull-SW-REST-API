"""empty message

Revision ID: 958cde332d11
Revises: a5708c49865d
Create Date: 2024-03-29 18:51:21.031034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '958cde332d11'
down_revision = 'a5708c49865d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=50),
               existing_nullable=False)

    with op.batch_alter_table('city', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=50),
               existing_nullable=False)

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=50),
               existing_nullable=False)

    with op.batch_alter_table('starships', schema=None) as batch_op:
        batch_op.add_column(sa.Column('model', sa.String(length=50), nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=50),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('surname',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)
        batch_op.alter_column('surname',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)

    with op.batch_alter_table('starships', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)
        batch_op.drop_column('model')

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)

    with op.batch_alter_table('city', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)

    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)

    # ### end Alembic commands ###