/*
 * static.h
 *
 *  Created on: Dec 10, 2021
 *      Author: skauffma
 *
 *   nfer - a system for inferring abstractions of event streams
 *   Copyright (C) 2021  Sean Kauffman
 *
 *   This file is part of nfer.
 *   nfer is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 3 of the License, or
 *   (at your option) any later version.
 *
 *   This program is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

#ifndef INC_STATIC_H_
#define INC_STATIC_H_

#include "ast.h"
#include "nfer.h"

typedef struct _rule_digraph_vertex {
    ast_node      *rule;
    unsigned int  incoming; /* number of incoming edges */
    bool          removed;  /* used in the topological sort algorithm */
} rule_digraph_vertex;

typedef struct _rule_digraph_edge {
    struct _rule_digraph_vertex    *from;
    struct _rule_digraph_vertex    *to;
    bool          removed;  /* used in the topological sort algorithm */
} rule_digraph_edge;

void initialize_analysis(spec_analysis *);
bool do_static_analysis(ast_node **, spec_analysis *);

#endif /* INC_STATIC_H_ */
