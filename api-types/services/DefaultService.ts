/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Add Task
     * @param name
     * @returns any Successful Response
     * @throws ApiError
     */
    public static addTaskApiTasksPost(
        name: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/tasks',
            query: {
                'name': name,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Tasks
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getTasksApiTasksGet(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/tasks',
        });
    }

    /**
     * Update Task
     * @param taskId
     * @param name
     * @returns any Successful Response
     * @throws ApiError
     */
    public static updateTaskApiTasksUpdatePost(
        taskId: number,
        name: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/tasks/update',
            query: {
                'task_id': taskId,
                'name': name,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Complete Task
     * @param taskId
     * @param timeIsoString
     * @returns any Successful Response
     * @throws ApiError
     */
    public static completeTaskApiTasksCompletePost(
        taskId: number,
        timeIsoString: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/tasks/complete',
            query: {
                'task_id': taskId,
                'time_iso_string': timeIsoString,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Complete Task
     * @param taskId
     * @returns any Successful Response
     * @throws ApiError
     */
    public static completeTaskApiTasksIncompletePost(
        taskId: number,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/tasks/incomplete',
            query: {
                'task_id': taskId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Play Task
     * @param taskId
     * @param timeIsoString
     * @returns any Successful Response
     * @throws ApiError
     */
    public static playTaskApiTasksPlayPost(
        taskId: number,
        timeIsoString: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/tasks/play',
            query: {
                'task_id': taskId,
                'time_iso_string': timeIsoString,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Pause Task
     * @param taskId
     * @param timeIsoString
     * @returns any Successful Response
     * @throws ApiError
     */
    public static pauseTaskApiTasksPausePost(
        taskId: number,
        timeIsoString: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/tasks/pause',
            query: {
                'task_id': taskId,
                'time_iso_string': timeIsoString,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
