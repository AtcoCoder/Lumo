"""Initial migration

Revision ID: 1e7e2f436820
Revises: 
Create Date: 2024-12-23 00:02:48.575506

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1e7e2f436820'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('amenities', 'name',
               existing_type=mysql.VARCHAR(length=16),
               type_=sa.String(length=32),
               existing_nullable=False)
    op.alter_column('areas', 'name',
               existing_type=mysql.VARCHAR(length=16),
               type_=sa.String(length=60),
               existing_nullable=False)
    op.alter_column('cities', 'name',
               existing_type=mysql.VARCHAR(length=16),
               type_=sa.String(length=60),
               existing_nullable=False)
    op.alter_column('regions', 'name',
               existing_type=mysql.VARCHAR(length=16),
               type_=sa.String(length=60),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('regions', 'name',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=16),
               existing_nullable=False)
    op.alter_column('cities', 'name',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=16),
               existing_nullable=False)
    op.alter_column('areas', 'name',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=16),
               existing_nullable=False)
    op.alter_column('amenities', 'name',
               existing_type=sa.String(length=32),
               type_=mysql.VARCHAR(length=16),
               existing_nullable=False)
    # ### end Alembic commands ###
