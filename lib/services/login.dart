// To parse this JSON data, do
//
//     final login = loginFromJson(jsonString);

// ignore_for_file: use_build_context_synchronously

import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:smart_farming/bottom_navbar.dart';
import 'package:smart_farming/constants/constants.dart';
import 'package:smart_farming/soil_input.dart';

Login loginFromJson(String str) => Login.fromJson(json.decode(str));

String loginToJson(Login data) => json.encode(data.toJson());

class Login {
  String message;

  Login({
    required this.message,
  });

  factory Login.fromJson(Map<String, dynamic> json) => Login(
        message: json["message"],
      );

  Map<String, dynamic> toJson() => {
        "message": message,
      };
}

// This function logs in the user by sending a POST request to the server.
Future login(
  BuildContext context,
  String email,
  String password,
) async {
  try {
    String base = baseUri;
    String login = loginUri;
    final response = await http.post(
      Uri.parse("$base$login"),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, dynamic>{
        'email': email,
        'password': password,
      }),
    );

    String result = jsonDecode(response.body)['message'];
    if (response.statusCode == 200) {
      final Map<String, dynamic> userResult = jsonDecode(response.body);

      return Navigator.pushAndRemoveUntil(
        context,
        MaterialPageRoute(
          builder: (context) => const BottomNavBar(),
        ),
        (route) => false,
      );
    } else if (result == "Invalid Login credentials") {
      var error = ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: const Text(
            'Invalid Login credentials',
            style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.w500,
            ),
          ),
          backgroundColor: Theme.of(context).colorScheme.error,
          duration: const Duration(seconds: 1),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.all(
              Radius.circular(MediaQuery.of(context).size.width * 0.02),
            ),
          ),
          behavior: SnackBarBehavior.floating,
        ),
      );

      return error;
    } else {
      var error = ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: const Text(
            'Failed to Login User',
            style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.w500,
            ),
          ),
          backgroundColor: Theme.of(context).colorScheme.error,
          duration: const Duration(seconds: 1),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.all(
              Radius.circular(
                MediaQuery.of(context).size.width * 0.02,
              ),
            ),
          ),
          behavior: SnackBarBehavior.floating,
        ),
      );

      return error;
    }
  } catch (e) {
    print(e.toString());
    throw Exception('Failed to Login User: $e');
  }
}
