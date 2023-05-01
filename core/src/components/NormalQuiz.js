import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import ConnectApi from "../api/ConnectApi";
import Header from "./framework/Header";
import Footer from "./framework/Footer";

class NormalQuiz extends React.Component {
  state = {
    questions: [],
    currentQuestionIndex: 0,
    selectedAnswer: null,
    answerCorrect: null,
  };

  componentDidMount() {
    fetch(API_URL)
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          questions: data,
        });
      });
  }

  handleAnswerSelected = (answer) => {
    const { questions, currentQuestionIndex } = this.state;
    const isCorrect = answer === questions[currentQuestionIndex].correct_answer;

    this.setState({
      selectedAnswer: answer,
      answerCorrect: isCorrect,
    });
  };

  handleNextQuestion = () => {
    const { currentQuestionIndex, questions } = this.state;
    if (currentQuestionIndex < questions.length - 1) {
      this.setState({
        currentQuestionIndex: currentQuestionIndex + 1,
        selectedAnswer: null,
        answerCorrect: null,
      });
    }
  };

  render() {
    const { questions, currentQuestionIndex, selectedAnswer, answerCorrect } = this.state;

    if (questions.length === 0) {
      return <div>Loading...</div>;
    }

    const currentQuestion = questions[currentQuestionIndex];
    const answerOptions = currentQuestion.answer_options;

    return (
      <div>
        <Question
          question={currentQuestion.question}
          answerOptions={answerOptions}
          selectedAnswer={selectedAnswer}
          onAnswerSelected={this.handleAnswerSelected}
        />
        {answerCorrect !== null && (
          <Result
            answerCorrect={answerCorrect}
            onNextQuestion={this.handleNextQuestion}
          />
        )}
      </div>
    );
  }
}
export default NormalQuiz
