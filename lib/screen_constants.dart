import 'package:flutter/material.dart';

// Screen size constants and functions for responsiveness

// Logical pixel width thresholds for different screen sizes
const double mediumPhoneWidth = 375; // Medium phone width
const double largePhoneWidth = 410; // Large phone
const double tabletWidth = 768; // Tablet width

// Functions to check the current screen size based on the provided BuildContext
bool isMediumMobile(BuildContext context) =>
    MediaQuery.of(context).size.width >= mediumPhoneWidth &&
    MediaQuery.of(context).size.width < largePhoneWidth;

bool isLargeMobile(BuildContext context) =>
    MediaQuery.of(context).size.width >= largePhoneWidth &&
    MediaQuery.of(context).size.width < tabletWidth;
