/*
 * Copyright 2012 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.errorprone.suppliers;

import com.google.errorprone.VisitorState;
import com.sun.source.tree.ExpressionTree;
import com.sun.source.tree.MethodInvocationTree;
import com.sun.tools.javac.code.Type;
import com.sun.tools.javac.code.Type.ClassType;
import com.sun.tools.javac.tree.JCTree.JCExpression;
import com.sun.tools.javac.tree.JCTree.JCFieldAccess;

/**
 * @author alexeagle@google.com (Alex Eagle)
 */
public class Suppliers {

  /**
   * Supplies the n'th generic type of the given expression. For example, in {@code Map<A,B> c;} for the expression
   * c and n=1, the result is the type of {@code B}.
   * @param expressionSupplier a supplier of the expression which has a generic type
   * @param n the position of the generic argument
   */
  public static Supplier<Type> genericTypeOf(final Supplier<ExpressionTree> expressionSupplier, final int n) {
    return new Supplier<Type>() {
      @Override
      public Type get(VisitorState state) {
        JCExpression jcExpression = (JCExpression) expressionSupplier.get(state);
        return ((ClassType) jcExpression.type).typarams_field.get(n);
      }
    };
  }

  /**
   * Supplies the expression which gives the instance of an object that will receive the method call.
   * For example, in
   * {@code a.getB().getC()}
   * if the visitor is currently visiting the {@code getC()} method invocation, then this supplier gives the
   * expression {@code a.getB()}.
   */
  public static Supplier<ExpressionTree> receiverInstance() {
    return new Supplier<ExpressionTree>() {
      @Override
      public ExpressionTree get(VisitorState state) {
        MethodInvocationTree method = (MethodInvocationTree) state.getPath().getLeaf();
        return ((JCFieldAccess) method.getMethodSelect()).getExpression();
      }
    };
  }

  /**
   * Given the string representation of a type, supplies the corresponding type.
   *
   * @param typeString a string representation of a type, e.g., "java.util.List"
   */
  public static Supplier<Type> typeFromString(final String typeString) {
    return new Supplier<Type>() {
      @Override
      public Type get(VisitorState state) {
        return state.getTypeFromString(typeString);
      }
    };
  }

  /**
   * Supplies what was given. Useful for adapting to methods that require a supplier.
   *
   * @param toSupply the item to supply
   */
  public static <T> Supplier<T> identitySupplier(final T toSupply) {
    return new Supplier<T>() {
      @Override
      public T get(VisitorState state) {
        return toSupply;
      }
    };
  }
}
