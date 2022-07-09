#(c) 2018 Takashi Michikawa < michikawa@acm.org>
set(MI_LATEX_COMMAND  "xelatex")
set(MI_BIBTEX_COMMAND "bibtex")
# @todo function だと <TARGET_NAME>_SOURCE_DIRの定義が必要(方法がわからなかかった．)
macro(add_tex_files TARGET_NAME TEX_MAIN_FILE)
        get_filename_component(MAIN_TEX_FILE_STEM ${TEX_MAIN_FILE} NAME_WE) # e.g. TEX_MAIN_FILE = main.tex MAIN_TEX_FILE_STEM = main
        if (${CMAKE_VERBOSE_MAKEFILE} EQUAL 1)
	# do nothing 	
	else ()
                set(REDIRECTION ">")
                if (WIN32)
                        set(DEV_NULL "nul")
                else() # (UNIX)
                        set(DEV_NULL "/dev/null")
                endif()
        endif()
	
	#ファイルを (1) bibファイル (2)それ以外 に分ける bibファイルがある場合は，bibtexをかける
	#        if ( ${ARGC} GREATER 2 )
	#        set(args ${ARGN} "" "")
	#        set(OTHER_FILES "")
	#        foreach(loop_var IN LISTS args)
	#                if ( "${loop_var}" MATCHES ".*bib") # ファイル内にbibファイルがある場合は分別
	#                        set (TEX_BIB_FILE ${TEX_BIB_FILE} ${loop_var})
	#                        set (BIB_TARGET ${TARGET_NAME}_bib)
	#                else()
	#                        set (OTHER_FILES ${OTHER_FILES} ${loop_var})
	#                endif()
	#        endforeach()
	#endif()

        add_custom_target (${TARGET_NAME} ALL
        	SOURCES ${MAIN_TEX_FILE_STEM}.pdf
		#        	DEPENDS ${BIB_TARGET} ${TARGET_NAME}_dvi
		)
        add_custom_command (OUTPUT  ${MAIN_TEX_FILE_STEM}.pdf
        	COMMAND ${CMAKE_COMMAND} -E env TEXINPUTS=$ENV{TEXINPUTS}:${CMAKE_CURRENT_SOURCE_DIR} ${MI_LATEX_COMMAND} --shell-escape ${TEX_MAIN_FILE} ${REDIRECTION} ${DEV_NULL}
        	COMMAND ${CMAKE_COMMAND} -E env TEXINPUTS=$ENV{TEXINPUTS}:${CMAKE_CURRENT_SOURCE_DIR} ${MI_LATEX_COMMAND} --shell-escape ${TEX_MAIN_FILE} ${REDIRECTION} ${DEV_NULL}
		)
	#        add_custom_target ( ${TARGET_NAME}_bib
		#	SOURCES ${MAIN_TEX_FILE_STEM}.bbl
		#        	DEPENDS ${TARGET_NAME}_dvi
		#		)
		#	add_custom_command (OUTPUT ${MAIN_TEX_FILE_STEM}.bbl
		#		COMMAND ${CMAKE_COMMAND} -E env BIBINPUTS=$ENV{BIBINPUTS}:${CMAKE_CURRENT_SOURCE_DIR} ${MI_BIBTEX_COMMAND} ${MAIN_TEX_FILE_STEM} ${REDIRECTION} ${DEV_NULL}
		#		DEPENDS ${TEX_BIB_FILE}
		#		)
	
		#	add_custom_target ( ${TARGET_NAME}_dvi
		#		SOURCES ${MAIN_TEX_FILE_STEM}.aux
		#		)
		#        add_custom_command (OUTPUT ${MAIN_TEX_FILE_STEM}.aux
		#                COMMAND ${CMAKE_COMMAND} -E env TEXINPUTS=$ENV{TEXINPUTS}:${CMAKE_CURRENT_SOURCE_DIR} ${MI_LATEX_COMMAND} -draftmode ${TEX_MAIN_FILE} ${MI_REDIRECT_TO_DEV_NULL} ${REDIRECTION} ${DEV_NULL}
		#                DEPENDS ${OTHER_FILES}
		#		)
endmacro()
