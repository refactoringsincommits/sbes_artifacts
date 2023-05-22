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

package com.google.errorprone.bugpatterns;

import com.google.errorprone.BugPattern;
import com.google.errorprone.VisitorState;
import com.google.errorprone.fixes.SuggestedFix;
import com.google.errorprone.matchers.DescribingMatcher;
import com.google.errorprone.matchers.Description;
import com.sun.source.tree.EmptyStatementTree;

import static com.google.errorprone.BugPattern.Category.JDK;
import static com.google.errorprone.BugPattern.MaturityLevel.MATURE;
import static com.google.errorprone.BugPattern.SeverityLevel.WARNING;

/**
 * This checker finds and fixes empty statements, for example:
 * if (foo == 10);
 * ;
 *
 * @author eaftan@google.com (Eddie Aftandilian)
 */
@BugPattern(name = "EmptyStatement",
    summary = "Empty statement",
    explanation =
        "An empty statement has no effect on the program. Consider removing it.",
    category = JDK, severity = WARNING, maturity = MATURE)
public class EmptyStatement extends DescribingMatcher<EmptyStatementTree> {

  @Override
  public boolean matches(EmptyStatementTree emptyStatementTree, VisitorState state) {
    return true;
  }

  @Override
  public Description describe(
      EmptyStatementTree emptyStatementTree, VisitorState state) {
    return new Description(
        emptyStatementTree,
        getDiagnosticMessage(),
        new SuggestedFix().delete(emptyStatementTree));
  }

}