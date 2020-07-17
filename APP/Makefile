#!make
ifneq (, $(wildcard Makefile-env))
	include Makefile-env
endif
export $(shell sed 's/=.*//' Makefile-env)

build-fe:
	ng build --prod --base-href=./sources/angular
	manage.py collectstatic