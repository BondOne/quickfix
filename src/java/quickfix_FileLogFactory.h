/* DO NOT EDIT THIS FILE - it is machine generated */
#include <jni.h>
/* Header for class quickfix_FileLogFactory */

#ifndef _Included_quickfix_FileLogFactory
#define _Included_quickfix_FileLogFactory
#ifdef __cplusplus
extern "C" {
#endif
/*
 * Class:     quickfix_FileLogFactory
 * Method:    create
 * Signature: ()V
 */
JNIEXPORT void JNICALL Java_quickfix_FileLogFactory_create__
  (JNIEnv *, jobject);

/*
 * Class:     quickfix_FileLogFactory
 * Method:    destroy
 * Signature: ()V
 */
JNIEXPORT void JNICALL Java_quickfix_FileLogFactory_destroy
  (JNIEnv *, jobject);

/*
 * Class:     quickfix_FileLogFactory
 * Method:    create
 * Signature: (Lquickfix/SessionID;)Lquickfix/Log;
 */
JNIEXPORT jobject JNICALL Java_quickfix_FileLogFactory_create__Lquickfix_SessionID_2
  (JNIEnv *, jobject, jobject);

#ifdef __cplusplus
}
#endif
#endif